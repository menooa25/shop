import React, { Component } from "react";
import CheckUserAuth from "../../utils/checkUserAuth";

class Buy extends Component {
  state = { discount: 0, totalPrice: 0, discountCode: "" };
  render() {
    if (this.props.totalPrice) {
      this.setState({ totalPrice: this.props.totalPrice });
    }
    return (
      <>
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
              جمع کل سبد خرید:{" "}
              <span className="text-success">
                {" "}
                {this.state.totalPrice && this.state.totalPrice} تومان
              </span>
            </span>
          </div>{" "}
          <hr />
          <div>
            <span>
              جمع کل:{" "}
              <span className="text-success">
                {" "}
                {this.state.totalPrice &&
                  this.state.totalPrice - this.state.discount}{" "}
                تومان
              </span>
            </span>
          </div>
        </div>
        <div className="rounded shadow bg-white p-2 mt-2">
          {/* first discount code will check if its valid it will apply and show to user */}
          <form onSubmit={this.handleOnCheckDiscount}>
            <div className="form-group">
              <label htmlFor="code">کد تخفیف</label>
              <input
                type="text"
                name="code"
                id="code"
                className="form-control"
                dir="ltr"
              />
            </div>
            <button type="btn" className="form-control btn btn-outline-danger">
              اعمال کد تخفیف
            </button>
          </form>
        </div>
        <div>
          <button
            onClick={this.handleOnBuy}
            className="btn btn-success form-control mt-2 shadow"
          >
            تسویه حساب
          </button>
        </div>
      </>
    );
  }
  handleOnBuy = () => {
    CheckUserAuth();
    const form = new FormData();
    form.set("code", this.state.discountCode);
    const headers = new Headers();
    const token = sessionStorage["token"];
    headers.set("Authorization", token);
    fetch("http://127.0.0.1:8000/api/v1/orders/add_to_checkout", {
      method: "POST",
      headers,
      body: form,
    });
  };
  handleOnCheckDiscount = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    const headers = new Headers();
    const token = sessionStorage["token"];
    headers.set("Authorization", token);
    fetch("http://127.0.0.1:8000/api/v1/orders/discount", {
      headers,
      body: form,
      method: "POST",
    })
      .then((res) => res.json())
      //  setting discount percent times total price
      .then((res) => {
        this.setState({
          discount: this.state.totalPrice * (res / 100),
          discountCode: form.get("code"),
        });
      });
  };
  shouldComponentUpdate(nextProps, nextState, nextContext) {
    if (
      this.props.totalPrice === this.state.totalPrice &&
      this.state.discount === nextState.discount
    )
      return false;
    return true;
  }
}

export default Buy;
