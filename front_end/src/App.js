import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import ProductContainer from "./components/products/productContainer";

class App extends Component {
  render() {
    return (
      <div>
        <header className="container d-flex justify-content-between mt-3">
          <div>
            <button className="btn btn-outline-danger">Hello</button>
          </div>
          <div>
            <form className="form-inline my-2 my-lg-0">
              <input
                className="form-control mr-sm-2"
                type="search"
                placeholder="به دنبال چه چیزی میگردید؟"
              />
              <button
                className="btn btn-outline-success my-2 my-sm-0"
                type="submit"
              >
                جستجو
              </button>
            </form>
          </div>
          <div>
            <button className="btn rounded-circle  btn-outline-success">
              ۲۵
            </button>
          </div>
        </header>
        <ProductContainer/>
      </div>
    );
  }
}

export default App;
