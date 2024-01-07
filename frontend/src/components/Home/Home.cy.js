import Home from "./Home";

describe("Home", () => {
  it("renders home with a heading", () => {
    cy.mount(<Home />);
    cy.get('[data-cy="head-content"]').should("contain.text", "Roammates");
  });
});
