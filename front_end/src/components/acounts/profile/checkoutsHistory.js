import React, { useEffect, useState } from "react";

function CheckoutsHistory(props) {
  const [checkout_history, setCheckoutHistory] = useState(null);
  // getting user checkout history
  useEffect(() => {
    const header = new Headers();
    const token = sessionStorage["token"];
    header.set("Authorization", token);
    fetch("http://127.0.0.1:8000/api/v1/orders/orders_history", {
      headers: header,
      method: "GET",
    })
      .then((res) => res.json())
      .then((res) => {
        if (res) setCheckoutHistory(res);
      });
  }, []);
  return (
    <div dir="rtl" className="text-right bg-white p-2 shadow rounded mr-3">
      {checkout_history &&
        checkout_history.map((checkout) => {
          return (
            <div className="d-flex flex-column">
              <div> جمع کل: {checkout.total_price} تومان </div>
              <p>وضعیت: {checkout.status}</p>
              {checkout.product.map((p) => {
                return (
                  <div dir="rtl" className="text-right">
                    <p className="d-inline">{p.quantity}</p>
                    <p className="d-inline"> عدد {p.name}</p>
                  </div>
                );
              })}
              <hr />
            </div>
          );
        })}
    </div>
  );
}

export default CheckoutsHistory;
