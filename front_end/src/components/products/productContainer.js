import React, { Component } from "react";

class ProductContainer extends Component {
  render() {
    return (
      <div className="bg-light pt-3" style={{ height: "100vh" }}>
        <main className="mt-3 w-75 ml-auto">
          <div className="row">
            <article className="col-8">
              <div className="row">
                <div className="col-3 px-2 card-height">
                  <div className="card-body shadow rounded " >
                    <img
                      src="https://picsum.photos/id/871/200/500"
                      className="card-img rounded"
                    />
                    <h3>Lorem ipsum dolor sit amet.</h3>
                  </div>
                </div><div className="col-3 px-2 card-height">
                  <div className="card-body shadow rounded " >
                    <img
                      src="https://picsum.photos/id/870/200/500"
                      className="card-img rounded"
                    />
                    <h3>Lorem ipsum dolor sit amet.</h3>
                  </div>
                </div><div className="col-3 px-2">
                  <div className="card-body shadow rounded " >
                    <img
                      src="https://picsum.photos/id/869/200/200"
                      className="card-img rounded"
                    />
                    <h3>Lorem ipsum dolor sit amet.</h3>
                  </div>
                </div>
              </div>
            </article>
            <aside className="col-4"></aside>
          </div>
        </main>
      </div>
    );
  }
}

export default ProductContainer;
