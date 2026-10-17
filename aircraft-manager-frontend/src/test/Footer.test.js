// Import necessary libraries and the Footer component for testing
import React from 'react';
import { render, screen } from '@testing-library/react';
import Footer from '../components/Footer';

// Group tests related to the Footer component
describe('Footer Component', () => {
  // Test case to verify that the Footer component renders without throwing errors
  it('renders without crashing', () => {
    render(<Footer />);
    // Check if the text "contact us" is present in the document, which indicates the component rendered successfully
    expect(screen.getByText(/contact us/i)).toBeInTheDocument();
  });

  // Test case to ensure the Footer displays the correct contact information
  it('displays correct contact info', () => {
    render(<Footer />);
    // Verify that the email address is displayed in the footer
    expect(screen.getByText('contact@pythonairways.com')).toBeInTheDocument();
    // Verify that the phone number is correctly displayed in the footer
    expect(screen.getByText('+1 (123) 456-7890')).toBeInTheDocument();
  });

  // Test case to check if social media links in the Footer have correct href attributes
  it('contains social media links with correct hrefs', () => {
    render(<Footer />);

    // Assuming the second link is to Twitter, based on the structure of the component
    const twitterLink = screen.getAllByRole('link', { name: '' })[1].closest('a');
    // Assuming the third link is to Instagram, based on the structure of the component
    const instagramLink = screen.getAllByRole('link', { name: '' })[2].closest('a');

    // Check that the Twitter link navigates to the correct URL
    expect(twitterLink).toHaveAttribute('href', 'https://www.twitter.com');
    // Check that the Instagram link navigates to the correct URL
    expect(instagramLink).toHaveAttribute('href', 'https://www.instagram.com');
  });

  // Test case to verify that the Footer contains links to Privacy Policy and Terms of Service, and they navigate to correct paths
  it('contains privacy and terms of service links', () => {
    render(<Footer />);
    // Check the Privacy Policy link is present and navigates to the correct path
    expect(screen.getByText(/privacy policy/i).closest('a')).toHaveAttribute('href', '/privacy');
    // Check the Terms of Service link is present and navigates to the correct path
    expect(screen.getByText(/terms of service/i).closest('a')).toHaveAttribute('href', '/terms');
  });

});