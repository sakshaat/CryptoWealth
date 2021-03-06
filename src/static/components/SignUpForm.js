import React from 'react';
import t from 'tcomb-form';
import { bindActionCreators } from 'redux';
import * as actionCreators from '../actions/auth';
import { connect } from 'react-redux';
import classNames from 'classnames';


const Form = t.form.Form;

const SignUp = t.struct({
  email: t.String,
  username: t.String,
  password: t.String
});

const SignUpFormOptions = {
  auto: 'placeholders',
  help: '',
  fields: {
    password: {
      type: 'password'
    }
  }
};


class SignUpForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            formValues: {
                email: '',
                password: '',
                username: ''
            },
            redirectRoute: "/login"
        };
    }

    static propTypes = {
        dispatch: React.PropTypes.func.isRequired,
        isAuthenticating: React.PropTypes.bool.isRequired,
        statusText: React.PropTypes.string,

        investment: React.PropTypes.oneOfType([
            React.PropTypes.string,
            React.PropTypes.number,
        ]),

        riskLevel: React.PropTypes.number.isRequired
    };

    onFormChange = (value) => {
        this.setState({ formValues: value });
    };

    signup = (e) => {
        e.preventDefault();
        const value = this.signUpForm.getValue();
        if (value) {
            this.props.actions.authSignUpUser(value.username,
                value.password, value.email, this.props.investment, this.props.riskLevel,
                this.state.redirectRoute);
        }
    };

    render() {
        let statusText = null;

        if (this.props.statusText) {
        const statusTextClassNames = classNames({
            'alert': true,
            'alert-danger': this.props.statusText.indexOf('Authentication Error') === 0,
            'alert-success': this.props.statusText.indexOf('Authentication Error') !== 0
        });

        statusText = (
            <div className="row">
                <div className="col-sm-12">
                    <div className={statusTextClassNames}>
                    {this.props.statusText}
                    </div>
                </div>
            </div>
            );
        }


        return(
            <div className="login">
                <h1 className="text-center">Only 1 step away!</h1>
                <h1 className="text-center">Join us to start investing:</h1>
                <div className="login-container margin-top-medium">
                {statusText}

                    <form onSubmit={this.signup}>
                        <Form ref={(ref) => { this.signUpForm = ref; }}
                                type={SignUp}
                                options={SignUpFormOptions}
                                value={this.state.formValues}
                                onChange={this.onFormChange}
                        />
                        <button
                            disabled={this.props.isAuthenticating}
                            type="submit"

                            className="btn btn-default btn-block hero-button">
                              <span className="heroButtonText">
                                Start Investing
                              </span>
                        </button>
                    </form>
                </div>
            </div>)
        }
}


const mapStateToProps = (state) => {
  return {
    investment: state.quest.investment,
    riskLevel: state.quest.riskLevel,
    isAuthenticating: state.auth.isAuthenticating,
    statusText: state.auth.statusText
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    dispatch,
    actions: bindActionCreators(actionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignUpForm);
export { SignUpForm };
