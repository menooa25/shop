import React, { Component } from "react";
import ProductShow from "./productShow";

class ProductContainer extends Component {
  state = { products: null };

  render() {
    return (
      <div className="bg-light pt-3" style={{ height: "100vh" }}>
        <main className="mt-1 w-75 ml-auto">
          <div className="row">
            <article className="col-8">
              <div className="row">
                {this.state.products &&
                  this.state.products.map((product) => (
                    <ProductShow key={product.id} product={product} />
                  ))}
              </div>
            </article>
            <aside className="col-4"></aside>
          </div>
        </main>
      </div>
    );
  }

  // getting products to show
  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/v1/products/")
      .then((res) => res.json())
      .then((res) => this.setState({ products: res }));
  }
}

export default ProductContainer;
