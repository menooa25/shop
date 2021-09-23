import React, { Component } from "react";
import Buy from "./buy";
import Orders from "./orders";

class Basket extends Component {
  state = { totalPrice: "" };
  render() {
    return (
      <div className="bg-light h-100vh">
        <div className="container pt-3">
          <div className="row m-0">
            <div dir="rtl" className="text-right col-4">
              <h5>خلاصه فاکتور</h5>
              <Buy
                totalPrice={this.state.totalPrice && this.state.totalPrice}
              />
            </div>
            <div dir="rtl" className="text-right col-8">
              <h5>محتویات سبد خرید</h5>
              <Orders totalPrice={this.handleTotalPrice} />
            </div>
          </div>
        </div>
      </div>
    );
  }
  handleTotalPrice = (totalPrice) => {
    this.setState({ totalPrice });
  };
}

export default Basket;
