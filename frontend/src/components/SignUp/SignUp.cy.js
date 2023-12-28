import SignUp from "./SignUp"

const navigate = () => {}

describe("Signing up", () => {
  it("After sign up, redirects to the /login page", () => {
    cy.mount(<SignUp navigate={navigate}/>)

    cy.get('[data-cy="signup-heading"]').should('contain.text', "Sign Up")
    
    })

  it("After sign up, redirects to the /login page", () => {
    cy.mount(<SignUp navigate={navigate}/>)

    const testData = {
      email: 'test@example.com',
      password: 'Test@123',
      confirmPassword: 'Test@123',
      userName: 'test_user',
    };

    // Fill out the form
    cy.get('[data-cy=signup-heading]').should('be.visible');
    cy.get('[name=email]').type(testData.email);
    cy.get('[name=password]').type(testData.password);
    cy.get('[name=confirmPassword]').type(testData.confirmPassword);
    cy.get('[name=userName]').type(testData.userName);

    // Submit the form
    cy.get('[data-cy=signup-signup-button]').click();

    // Check for successful redirection
    cy.url().should('include', '/login');
    
    })
  })

