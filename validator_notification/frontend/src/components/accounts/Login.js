import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { login } from "../../actions/auth";

export class Login extends Component {
  state = {
    username: localStorage.getItem("username")
      ? localStorage.getItem("username")
      : "",
    password: "",
  };

  static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool,
  };

  onSubmit = (e) => {
    e.preventDefault();
    this.props.login(this.state.username.toLowerCase(), "pruebas1");
    localStorage.setItem("username", this.state.username);
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />
    }

    const { username, password } = this.state;
    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Usuario (Ofidona):</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
              />
            </div>
            {/* <div className="form-group">
              <label>Contraseña</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
              />
            </div> */}
            <div className="form-group">
              <button type="submit" className="btn btn-accept">
                Entrar
              </button>
            </div>
            {/* <p>
              ¿No tienes cuenta? <Link to="/register">Registrarse</Link>
            </p> */}
          </form>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { login })(Login);
