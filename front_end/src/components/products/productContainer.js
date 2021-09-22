import React, { Component } from "react";
import ProductShow from "./productShow";
import Category from "./category";

class ProductContainer extends Component {
  state = { products: null };

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
                  this.state.products.map((product) => (
                    <ProductShow key={product.id} product={product} />
                  ))}
              </div>
            </article>
          </div>
        </main>
      </div>
    );
  }

  categoryValue = (value) => {
    // if value is -1 that means we should show all products
    if (value == -1) this.gettingAllProducts();
    else
      fetch(`http://127.0.0.1:8000/api/v1/products/category/${value}`)
        .then((res) => res.json())
        .then((res) => this.setState({ products: res }));
  };

  gettingAllProducts = () => {
    fetch("http://127.0.0.1:8000/api/v1/products/")
      .then((res) => res.json())
      .then((res) => this.setState({ products: res }));
  };

  // getting products to show
  componentDidMount() {
    this.gettingAllProducts();
  }
}

export default ProductContainer;
