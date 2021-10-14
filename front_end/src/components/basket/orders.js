import React, { Component } from "react";
import Order from "./order";
import SiteURL from "../../utils/url";

class Orders extends Component {
  state = { orders: null };
  render() {
    if (this.state.orders)
      return (
        <div>
          {this.state.orders.map((order) => (
            <Order
              key={order.product.name}
              product={order.product}
              quantity={order.quantity}
            />
          ))}
        </div>
      );
    return <></>;
  }
  totalPrice = () => {
    let total_price = 0;
    for (let order of this.state.orders) {
      total_price += order.product.price * order.quantity;
    }
    this.props.totalPrice(total_price);
  };
  componentDidMount() {
    const headers = new Headers();
    const token = sessionStorage["token"];
    headers.set("Authorization", token);
    fetch(SiteURL + "/api/v1/orders/basket", { headers })
      .then((res) => res.json())
      .then((res) => {
        this.setState({ orders: res });
        this.totalPrice();
      });
  }
}

export default Orders;
