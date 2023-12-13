import SignUp from "./SignUp"

const navigate = () => {}

describe("Signing up", () => {
  it("After sign up, redirects to the /login page", () => {
    cy.mount(<SignUp navigate={navigate}/>)
    cy.get('[data-cy="signup-heading"]').should('contain.text', "Sign Up")

    })
  })
