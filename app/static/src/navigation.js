'use strict';

function NavButton(props) {
    return (
        <a href={props.link}>
            <button className={props.classNames} onClick={props.onClick}>
            {props.value}
            </button>
        </a>
    );
  }

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selected: 0,
        }
    }

    handleClick(i) {
        this.state.selected = i;
        console.log(this.state.selected);
    }

    render() {
        return (
            <div className="nav-bar">
                <NavButton 
                    link="/"
                    value="Home"
                    onClick={() => this.handleClick(0)}
                    classNames={this.state.selected === 0 ? "nav-button selected" : "nav-button"}
                />
                <NavButton
                    link="/hobbies"
                    value="Hobbies"
                    onClick={() => this.handleClick(1)}
                    classNames={this.state.selected === 1 ? "nav-button selected" : "nav-button"}
                />
                <NavButton
                    link="/map"
                    value="Map"
                    onClick={() => this.handleClick(2)}
                    classNames={this.state.selected === 2 ? "nav-button selected" : "nav-button"}
                />
                <NavButton
                    link="/timeline"
                    value="Timeline"
                    onClick={() => this.handleClick(3)}
                    classNames={this.state.selected === 3 ? "nav-button selected" : "nav-button"}
                />
            </div>
        )
    }
}

let domContainer = document.querySelector('#navbar_container');
let root = ReactDOM.createRoot(domContainer);
root.render(<NavBar />);