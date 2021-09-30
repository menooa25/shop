import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CheckUserAuth from "../../utils/checkUserAuth";

const ProductPage = () => {
  const [id] = useState(useParams().id);
  const [product, setProduct] = useState(null);
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/v1/products/${id}`)
      .then((res) => res.json())
      .then((res) => setProduct(res));
  }, []);
  const onBuy = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);

    const header = new Headers();
    const token = sessionStorage["token"];
    header.set("Authorization", token);
    fetch("http://127.0.0.1:8000/api/v1/orders/buy", {
      method: "POST",
      headers: header,
      body: form,
    });
    CheckUserAuth();
  };
  return (
    <div className="bg-light h-100vh">
      <div className="container pt-3">
        <div className="text-right row ">
          <div className="col-4">
            <div className="bg-white rounded shadow p-2">
              <p>
                <span className="text-success">{product && product.price}</span>{" "}
                : قیمت
              </p>
              <form onSubmit={onBuy} dir="rtl">
                <input
                  type="number"
                  name="product"
                  value={product && product.id}
                  hidden
                />
                <div className="form-group">
                  <label htmlFor="quantity">تعداد</label>
                  <input
                    className="form-control"
                    id="quantity"
                    type="number"
                    min={1}
                    name="quantity"
                    max={product && product.quantity}
                    defaultValue="1"
                  />
                </div>
                <button className="btn btn-primary form-control">خرید</button>
              </form>
            </div>
          </div>
          <div className="col-8">
            <div dir="rtl" className=" rounded shadow p-2 bg-white">
              {product && (
                <div className="d-flex flex-column">
                  {" "}
                  <div className="d-flex">
                    <img
                      src={"http://127.0.0.1:8000" + product.image}
                      className="ml-auto"
                      alt=""
                    />
                    <p className="p-3">{product.short_description}</p>
                  </div>
                  <h3 className="p-3"> مشخصات</h3>
                  <p>{product.long_description}</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductPage;
