'use strict';

function NavButton(props) {
    console.log(props.classNames)
    return (
        <a href={props.link} className={props.classNames} onClick={props.onClick}>
            {props.value}
        </a>
    );
  }

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selected: "intro",
        }
    }

    handleClick(page) {
        this.setState({
            selected: page,
        });
        console.log(this.state.selected);
    }

    render() {
        return (
            <div className="nav-bar">
                <NavButton 
                    link="#intro"
                    value="Home"
                    onClick={() => this.handleClick("intro")}
                    classNames={this.state.selected == "intro" ? "nav-button selected" : "nav-button"}
                />
                <NavButton
                    link="#about"
                    value="About"
                    onClick={() => this.handleClick("about")}
                    classNames={this.state.selected == "about" ? "nav-button selected" : "nav-button"}
                />
                <NavButton 
                    link="#experiences"
                    value="Experience"
                    onClick={() => this.handleClick("experience")}
                    classNames={this.state.selected == "experience" ? "nav-button selected" : "nav-button"}
                />
                <NavButton
                    link="#hobbies"
                    value="Hobbies"
                    onClick={() => this.handleClick("hobbies")}
                    classNames={this.state.selected == "hobbies" ? "nav-button selected" : "nav-button"}
                />
                <NavButton
                    link="/map"
                    value="Map"
                    onClick={() => this.handleClick("map")}
                    classNames={this.state.selected == "map" ? "nav-button selected" : "nav-button"}
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