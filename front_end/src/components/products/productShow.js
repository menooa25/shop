import React, { Component } from "react";
import { Link } from "react-router-dom";
import SiteURL from "../../utils/url";

class ProductShow extends Component {
  render() {
    const productData = this.props.product;
    return (
      <div className="col-3 px-2 mt-3  card-height">
        <div className="card-body shadow bg-white rounded product-card ">
          {/* adding image host url */}
          <Link to={"product_page/" + productData.id}>
            <img
              src={SiteURL + productData.image}
              className="card-img rounded"
            />
          </Link>

          {/* we only want to show 45 char of description  */}
          <h6>
            {productData.short_description.length > 45 &&
              productData.short_description.substr(0, 45) + "..."}
            {productData.short_description.length <= 45 &&
              productData.short_description}
          </h6>
          <div className="d-flex justify-content-between">
            <p dir="rtl">{productData.price} تومان</p>
            <Link to={"product_page/" + productData.id}>
              <i className="bi bi-bag btn-link" />
            </Link>
          </div>
        </div>
      </div>
    );
  }
}

export default ProductShow;
