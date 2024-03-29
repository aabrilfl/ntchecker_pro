import React, { Component, Fragment } from "react";
import Loader from 'react-loader-spinner';
import TotalTable from "./TotalTable";
import Table from "./Table";
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { getIndividualNotifications } from "../../actions/data";


function containsUser(username, list) {
  var i;
  for (i = 0; i < list.length; i++) {
    if (list[i].username === username) {
      return true;
    }
  }

  return false;
}

function getUsers(notifications) {
  var user;
  var users = [];
  notifications.map(function (notification) {
    user = notification.user;
    if (!containsUser(user.username, users) && user.is_active) {
      users.push(user);
    }
  });
  return users;
}



class LayoutDashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      general_id: this.props.match.params.id,
      redirect: false
    };
  }

  static propTypes = {
    individualNotifications: PropTypes.array.isRequired,
    getIndividualNotifications: PropTypes.func.isRequired,
  };

  componentWillMount() {
    this.props.individualNotifications = [];
    return { };
  }

  componentDidMount() {
    this.props.getIndividualNotifications({
      general_id: this.state.general_id,
    });
  }

  setRedirect = () => {
    this.setState({
      redirect: true
    })
  }
  renderRedirect = () => {
    if (this.state.redirect) {
      return <Redirect to='/data/dashboard' />
    }
  }

  render() {
    return (
      <Fragment>
        <br></br>
        {this.renderRedirect()}
        <button className="btn btn-link btn-back" onClick={this.setRedirect}>Atrás</button>
        <br/>
        <div className="notificationDetailed">
          {this.props.individualNotifications.length > 0 ? (
            <div>
              <div>
                <h1>{this.props.individualNotifications[0].general.title}</h1>
              </div>
              <hr></hr>
              <h3>Total</h3>
              <TotalTable notifications={this.props.individualNotifications} />
            </div>
          ) : (
              <div className="container">
                <br></br>
                <div className="container" style={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center"
                }}>
                  <h3>Recibiendo datos...</h3>
                </div>
                <div className="container" style={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center"
                }}>
                  <Loader
                    type="Oval"
                    color="#9FD574"
                    height={50}
                    width={50}  // timeout={10000} //10 secs
                  />
                </div>
              </div>
          )}
        </div>
        <hr></hr>
        <div className="container">
          {this.props.individualNotifications.length > 0 ? (
            <Table notifications={this.props.individualNotifications} users={getUsers(this.props.individualNotifications)} />
          ) : (
              <div></div>
            )}
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  individualNotifications: state.data.individualNotifications,
});

export default connect(mapStateToProps, { getIndividualNotifications })(
  LayoutDashboard
);
