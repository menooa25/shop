import React, { Component } from "react";

class ProductShow extends Component {
  render() {
    const productData = this.props.product;
    return (
      <div className="col-3 px-2 card-height">
        <div className="card-body shadow rounded product-card ">
          <img src={productData.image} className="card-img rounded" />
          {/* we only want to show 45 char of description  */}
          <h6>
            {productData.short_description.length > 45 &&
              productData.short_description.substr(0, 45) + "..."}
            {productData.short_description.length <= 45 &&
              productData.short_description}
          </h6>
          <div className="d-flex justify-content-between">
            <p dir="rtl">{productData.price} تومان</p>
            <i className="bi bi-bag btn-link" />
          </div>
        </div>
      </div>
    );
  }
}

export default ProductShow;
