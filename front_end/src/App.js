import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js.map";
import "bootstrap-icons/font/bootstrap-icons.css";
import ProductContainer from "./components/products/productContainer";
import { BrowserRouter as Router, Link, Route, Switch } from "react-router-dom";
import Register from "./components/acounts/register";
import Login from "./components/acounts/login";
import Profile from "./components/acounts/profile/profile";
import ProductPage from "./components/products/productPage";

class App extends Component {
  render() {
    return (
      <Router>
        <header className="container d-flex justify-content-between my-2 mt-3">
          <div className="d-flex">
            <Link className="bi-person-circle icons text-info" to="login" />
            <Link className="bi-basket2 ml-2 icons text-info" to="basket" />
            <div className="ml-3">
              <p className="text-muted small mb-0">با ما تماس بگیرید</p>
              <p className="mb-0 text-muted small">۰۲۱-۱۲۳۴۵۶۷۸</p>
            </div>
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
            <Link to="/" className="alert-link">
              اسم فروشگاه
            </Link>
          </div>
        </header>

        <Switch>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/profile">
            <Profile />
          </Route>
          <Route path="/product_page/:id">
            <ProductPage />
          </Route>
          <Route path="/">
            <ProductContainer />
          </Route>
        </Switch>
      </Router>
    );
  }
}

export default App;
