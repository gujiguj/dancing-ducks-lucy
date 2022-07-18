'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function NavButton(props) {
    console.log(props.classNames);
    return React.createElement(
        "a",
        { href: props.link },
        React.createElement(
            "button",
            { className: props.classNames, onClick: props.onClick },
            props.value
        )
    );
}

var NavBar = function (_React$Component) {
    _inherits(NavBar, _React$Component);

    function NavBar(props) {
        _classCallCheck(this, NavBar);

        var _this = _possibleConstructorReturn(this, (NavBar.__proto__ || Object.getPrototypeOf(NavBar)).call(this, props));

        _this.state = {
            selected: "intro"
        };
        return _this;
    }

    _createClass(NavBar, [{
        key: "handleClick",
        value: function handleClick(page) {
            this.setState({
                selected: page
            });
            console.log(this.state.selected);
        }
    }, {
        key: "render",
        value: function render() {
            var _this2 = this;

            return React.createElement(
                "div",
                { className: "nav-bar" },
                React.createElement(NavButton, {
                    link: "#intro",
                    value: "Home",
                    onClick: function onClick() {
                        return _this2.handleClick("intro");
                    },
                    classNames: this.state.selected == "intro" ? "nav-button selected" : "nav-button"
                }),
                React.createElement(NavButton, {
                    link: "#about",
                    value: "About",
                    onClick: function onClick() {
                        return _this2.handleClick("about");
                    },
                    classNames: this.state.selected == "about" ? "nav-button selected" : "nav-button"
                }),
                React.createElement(NavButton, {
                    link: "#hobbies",
                    value: "Hobbies",
                    onClick: function onClick() {
                        return _this2.handleClick("hobbies");
                    },
                    classNames: this.state.selected == "hobbies" ? "nav-button selected" : "nav-button"
                }),
                React.createElement(NavButton, {
                    link: "#map",
                    value: "Map",
                    onClick: function onClick() {
                        return _this2.handleClick("map");
                    },
                    classNames: this.state.selected == "map" ? "nav-button selected" : "nav-button"
                }),
                React.createElement(NavButton, {
                    link: "#timeline",
                    value: "Timeline",
                    onClick: function onClick() {
                        return _this2.handleClick(3);
                    },
                    classNames: this.state.selected === 3 ? "nav-button selected" : "nav-button"
                })
            );
        }
    }]);

    return NavBar;
}(React.Component);

var domContainer = document.querySelector('#navbar_container');
var root = ReactDOM.createRoot(domContainer);
root.render(React.createElement(NavBar, null));