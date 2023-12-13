import LoginPage from "./LoginPage"

const navigate = () => {}

describe("Logging In", () => {
  it("Renders the login component with the correct data", () => {
    cy.mount(<LoginPage navigate={navigate}/>)
    cy.get('[data-cy="login-heading"]').should('contain.text', "Login")
    })
  })
