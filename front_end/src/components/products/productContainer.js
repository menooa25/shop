import React, { Component } from "react";
import ProductShow from "./productShow";
import Category from "./category";
import SiteURL from "../../utils/url";

class ProductContainer extends Component {
  state = { products: null, page: 0, no_pages: 1 };

  render() {
    return (
      <div className="bg-light " style={{ height: "100vh" }}>
        <main className=" container">
          <div className="row">
            <div className="col-12">
              <Category value={this.categoryValue} />
            </div>
          </div>
          <div className="row">
            <article className="col-12">
              <div className="row">
                {this.state.products &&
                  this.state.products[this.state.page].map((product) => (
                    <ProductShow key={product.id} product={product} />
                  ))}
              </div>
            </article>
          </div>
          <div className="d-flex justify-content-center mt-5">
            <nav aria-label="Page navigation example">
              <ul className="pagination mb-2">
                <li className="page-item">
                  <a
                    className="page-link btn rounded-0"
                    onClick={() => this.increaseDecreasePage(-1)}
                  >
                    قبلی
                  </a>
                </li>
                {this.state.products &&
                  this.state.products.map((p, index) => {
                    return (
                      <li className="page-item">
                        <a
                          className="page-link btn rounded-0"
                          onClick={() => this.changePage(index)}
                        >
                          {index + 1}
                        </a>
                      </li>
                    );
                  })}

                <li className="page-item">
                  <a
                    className="page-link btn rounded-0"
                    onClick={() => this.increaseDecreasePage(+1)}
                  >
                    بعدی
                  </a>
                </li>
              </ul>
              <p className="mt-0 pt-0 text-center text-info">
                صفحه {this.state.page + 1}
              </p>
            </nav>
          </div>
        </main>
      </div>
    );
  }

  increaseDecreasePage = (operation) => {
    //  if operation is -1 it will decrease if its +1 it will increase
    if (operation === 1) {
      if (this.state.page + 1 < this.state.no_pages)
        this.setState({ page: this.state.page + 1 });
    } else {
      if (this.state.page !== 0) this.setState({ page: this.state.page - 1 });
    }
  };
  changePage = (page) => {
    this.setState({ page });
  };

  categoryValue = (value) => {
    // if value is -1 that means we should show all products
    if (value == -1) this.gettingAllProducts();
    else
      fetch(SiteURL + `/api/v1/products/category/${value}`)
        .then((res) => res.json())
        .then((res) => this.setState({ products: res, no_pages: res.length }));
  };

  gettingAllProducts = () => {
    fetch(SiteURL + "/api/v1/products/")
      .then((res) => res.json())
      .then((res) => this.setState({ products: res, no_pages: res.length }));
  };

  // getting products to show
  componentDidMount() {
    this.gettingAllProducts();
  }
}

export default ProductContainer;
