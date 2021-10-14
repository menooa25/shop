import React, { useEffect, useState } from "react";
import SiteURL from "../../../utils/url";

function DeliveredCheckoutHistory(props) {
  const [checkout_history, setCheckoutHistory] = useState(null);
  // getting user checkout history
  useEffect(() => {
    const header = new Headers();
    const token = sessionStorage["token"];
    header.set("Authorization", token);
    fetch(SiteURL + "/api/v1/orders/orders_history1", {
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
      {/* in every checkout there is a list of product so we need to use nested mapping */}
      {checkout_history &&
        checkout_history.map((checkout, index) => {
          return (
            <div key={index} className="d-flex flex-column p-2">
              <div> جمع کل: {checkout.total_price} تومان </div>
              <p className="mb-0">وضعیت: {checkout.status}</p>
              {checkout.product.map((p, index) => {
                return (
                  <div key={index} dir="rtl" className="text-right">
                    <p className="d-inline">{p.quantity}</p>
                    <p className="d-inline"> عدد {p.name}</p>
                  </div>
                );
              })}
            </div>
          );
        })}
    </div>
  );
}

export default DeliveredCheckoutHistory;
