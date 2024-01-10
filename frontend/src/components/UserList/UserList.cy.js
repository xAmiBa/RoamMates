import UserList from "./UserList";

const navigate = () => {};
describe("UserList", () => {
  it("renders User List with correct heading", () => {
    cy.mount(<UserList navigate={navigate} componentVersion="home" />);
    cy.get('[data-cy="test-heading"]').should(
      "contain.text",
      "Find Your Roam Mates!",
    );
  });

  it("renders User List with correct heading", () => {
    cy.mount(<UserList navigate={navigate} componentVersion="requests" />);
    cy.get('[data-cy="test-heading"]').should("contain.text", "Requests");
  });

  it("renders User List with correct heading", () => {
    cy.mount(<UserList navigate={navigate} componentVersion="matches" />);
    cy.get('[data-cy="test-heading"]').should("contain.text", "Matches");
  });
});
