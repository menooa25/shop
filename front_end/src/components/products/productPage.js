import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const ProductPage = () => {
  const [id] = useState(useParams().id);
  const [product, setProduct] = useState(null);
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/v1/products/${id}`)
      .then((res) => res.json())
      .then((res) => setProduct(res));
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col-4">
          <div>lorem50</div>
        </div>
        <div className="col-8">
          <div className="rounded shadow p-2 d-flex flex-column">
            {product && (
              <img
                src={"http://127.0.0.1:8000" + product.image}
                className="ml-auto"
                alt=""
              />
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductPage;
