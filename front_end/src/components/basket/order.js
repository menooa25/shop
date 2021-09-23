import React, { Component } from "react";

class Order extends Component {
  constructor(props) {
    super(props);

    const product = this.props.product;
    this.state = { ...product };
    this.state["quantity"] = this.props.quantity;
  }

  render() {
    return (
      <div className="bg-white rounded shadow p-3 mt-2 d-flex  text-right justify-content-between">
        <div dir="rtl">
          <h4>{this.state.name}</h4>
        </div>
        <div>
          <p>
            قیمت واحد:{" "}
            <span className="text-success">{this.state.price} تومان</span>
          </p>
          <p>
            قیمت کل:{" "}
            <span className="text-success">
              {this.state.price * this.state.quantity} تومان
            </span>
          </p>
        </div>
      </div>
    );
  }
}

export default Order;
