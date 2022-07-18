'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var NavButton = function (_React$Component) {
    _inherits(NavButton, _React$Component);

    function NavButton(props) {
        _classCallCheck(this, NavButton);

        var _this = _possibleConstructorReturn(this, (NavButton.__proto__ || Object.getPrototypeOf(NavButton)).call(this, props));

        _this.state = { selected: false };
        return _this;
    }

    _createClass(NavButton, [{
        key: "render",
        value: function render() {
            var _this2 = this;

            var classNames = this.state.selected ? "nav-button selected" : "nav-button";

            return React.createElement(
                "a",
                { href: this.props.link },
                React.createElement(
                    "button",
                    { className: "nav-button", onClick: function onClick() {
                            return _this2.setState({ selected: true });
                        } },
                    this.props.value
                )
            );
        }
    }]);

    return NavButton;
}(React.Component);

var NavBar = function (_React$Component2) {
    _inherits(NavBar, _React$Component2);

    function NavBar(props) {
        _classCallCheck(this, NavBar);

        return _possibleConstructorReturn(this, (NavBar.__proto__ || Object.getPrototypeOf(NavBar)).call(this, props));
    }

    _createClass(NavBar, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                React.createElement(NavButton, {
                    link: "/",
                    value: "Home"
                }),
                React.createElement(NavButton, {
                    link: "/hobbies",
                    value: "Hobbies"
                }),
                React.createElement(NavButton, {
                    link: "/map",
                    value: "Map"
                }),
                React.createElement(NavButton, {
                    link: "/timeline",
                    value: "Timeline"
                })
            );
        }
    }]);

    return NavBar;
}(React.Component);

var domContainer = document.querySelector('#navbar_container');
var root = ReactDOM.createRoot(domContainer);
root.render(React.createElement(NavBar, null));