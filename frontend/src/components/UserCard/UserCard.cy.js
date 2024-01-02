import UserCard from "./UserCard";

const testUser = {
    username: "test username",
    age: 20,
    gender: "male",
    bio: "test bio"
}

describe("UserCard", () => {
  it("renders UserCard with correct user's data", () => {
    cy.mount(<UserCard user={testUser}/>);
    cy.get('[data-cy="test-UserName"]').should("contain.text", "test username");
    cy.get('[data-cy="test-age"]').should("contain.text", "20");
    cy.get('[data-cy="test-gender"]').should("contain.text", "male");
    cy.get('[data-cy="test-bio"]').should("contain.text", "test bio");
  });
});
