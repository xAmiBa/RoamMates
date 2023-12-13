import FormField from "./FormField";

describe("Form Field", () => {
  it("renders FormField with correct label", () => {
    cy.mount(<FormField label="test" />);
    cy.get('[data-cy="form-label"]').should("contain.text", "test");
  });
});
