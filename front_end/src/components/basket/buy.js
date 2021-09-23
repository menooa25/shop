import React, { Component } from "react";

class Buy extends Component {
  state = { discount: 0 };
  render() {
    return (
      <div className="bg-white rounded shadow p-3">
        <div>
          <span>
            تخفیف:{" "}
            <span className="text-success">{this.state.discount} تومان</span>
          </span>
        </div>
        <hr />
        <div>
          <span>
            جمع کل:{" "}
            <span className="text-success">
              {" "}
              {this.props.totalPrice && this.props.totalPrice} تومان
            </span>
          </span>
        </div>
      </div>
    );
  }
}

export default Buy;
