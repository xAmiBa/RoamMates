import SideBar from "./SideBar";

const navigate = () => {}

describe("SideBar", () => {
    it('should render sidebar with correct link texts', () => {
        cy.mount(<SideBar navigate={navigate}/>)
        cy.get('[data-cy="button-text-content"]')
        .should("contain.text", "Home")
        .and("contain.text", "Matches")
        .and("contain.text", "Requests")
        .and("contain.text", "My Profile")
        .and("contain.text", "Log Out")
    }) 
})