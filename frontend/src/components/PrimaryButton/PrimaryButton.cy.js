import PrimaryButton from "./PrimaryButton";

describe("Primary Button", () => {
  it("renders Primary Button with correct text", () => {
    cy.mount(<PrimaryButton text="test" />);
    cy.get('[data-cy="button-text-content"]').should("contain.text", "test");
  });
});
