import React from 'react';
import { render, screen } from '@testing-library/react';
import PrivacyPolicy from '../components/PrivacyPolicy';

// Define a test suite for the PrivacyPolicy component to ensure it meets expected content standards
describe('PrivacyPolicy Component', () => {
  // Use beforeEach to DRY up the code by rendering the PrivacyPolicy component before each test
  beforeEach(() => {
    render(<PrivacyPolicy />);
  });

  // Test to verify that the main heading is rendered correctly
  it('renders the main heading', () => {
    const mainHeading = screen.getByRole('heading', { name: /privacy policy/i });
    expect(mainHeading).toBeInTheDocument(); // Checks if the heading is present in the document
  });

  // Test to ensure the introductory text of the privacy policy is displayed as expected
  it('displays introductory text correctly', () => {
    expect(screen.getByText(/welcome to our privacy policy/i)).toBeInTheDocument();
  });

  // Confirm that the statement emphasizing the importance of privacy is present
  it('confirms privacy importance statement', () => {
    expect(screen.getByText(/your privacy is important to us/i)).toBeInTheDocument();
  });

  // Verify the statement about information collection and consent is correctly displayed
  it('verifies information collection and consent statement', () => {
    expect(screen.getByText(/we only ask for personal information when we truly need it/i)).toBeInTheDocument();
  });

  // Additional tests to verify other key sections of the Privacy Policy

  // Ensure that the policy includes a statement about not sharing personal information
  it('mentions the non-sharing policy', () => {
    expect(screen.getByText(/we don't share any personally identifying information publicly/i)).toBeInTheDocument();
  });

  // Check for a disclaimer about external links not operated by the site
  it('addresses external links disclaimer', () => {
    expect(screen.getByText(/our website may link to external sites that are not operated by us/i)).toBeInTheDocument();
  });

  // Confirm the policy discusses the user's right to refuse to provide personal information
  it('discusses the right to refuse personal information', () => {
    expect(screen.getByText(/you are free to refuse our request for your personal information/i)).toBeInTheDocument();
  });

  // Verify the policy states that continued use of the site implies acceptance of privacy practices
  it('covers the acceptance of privacy practices through continued use', () => {
    expect(screen.getByText(/your continued use of our website will be regarded as acceptance/i)).toBeInTheDocument();
  });

  // Ensure the policy mentions its effective date, important for legal clarity
  it('includes the effective date of the policy', () => {
    expect(screen.getByText(/this policy is effective as of 1 April 2024/i)).toBeInTheDocument();
  });

  // Additional detailed tests can be added here to cover more specific aspects of the Privacy Policy content
});