import React from 'react';
import { render, screen } from '@testing-library/react';
import Terms from '../components/Terms';

// Grouping tests related to the Terms component to verify its content accuracy and completeness
describe('Terms Component Tests', () => {
    // Using beforeEach to render the Terms component before each test to ensure a fresh state
    beforeEach(() => {
      render(<Terms />);
    });
  
    // Testing that the main heading of the Terms and Conditions is correctly displayed
    it('should display the main heading', () => {
      // Expect the main heading to be present in the document
      expect(
        screen.getByRole('heading', { name: 'Terms and Conditions' })
      ).toBeInTheDocument();
    });
  
    // Verifying the introduction section that outlines the agreement for website usage
    it('should include the introduction about website usage agreement', () => {
      // Check for presence of text explaining user agreement to terms by using the website
      expect(
        screen.getByText(
          /if you continue to browse and use this website, you are agreeing to comply with and be bound by the following terms and conditions of use/i
        )
      ).toBeInTheDocument();
    });
  
    // Ensuring that the component mentions the possibility of content changes
    it('should mention the content change notice', () => {
      // Confirm text about content being subject to change is displayed
      expect(
        screen.getByText(/It is subject to change without notice./i)
      ).toBeInTheDocument();
    });
  
    // Confirming the disclaimer regarding the absence of warranties or guarantees for the website content
    it('should clarify the absence of warranty or guarantee', () => {
      // Look for a comprehensive disclaimer about no warranties or guarantees offered
      expect(
        screen.getByText(
          /Neither we nor any third parties provide any warranty or guarantee as to the accuracy, timeliness, performance, completeness, or suitability of the information and materials found or offered on this website for any particular purpose./i
        )
      ).toBeInTheDocument();
    });
  
    // Testing that there's a clear statement about the risk assumed by the user in using the website
    it('should state that website use is at the user\'s own risk', () => {
      // Verify the presence of a disclaimer about website use being at the user's own risk
      expect(
        screen.getByText(
          /Your use of any information or materials on this website is entirely at your own risk, for which we shall not be liable./i
        )
      ).toBeInTheDocument();
    });
  
    // Checking for a statement on copyright and ownership of materials present on the website
    it('should mention copyright and ownership of materials on the website', () => {
      // Assert that there's mention of material ownership and copyright
      expect(
        screen.getByText(
          /This website contains material which is owned by or licensed to us./i
        )
      ).toBeInTheDocument();
    });
  
    // Verifying acknowledgment of trademarks not owned or licensed by the website operator
    it('should acknowledge trademarks not owned or licensed to the operator', () => {
      // Confirm text acknowledging third-party trademarks is present
      expect(
        screen.getByText(
          /All trademarks reproduced in this website, which are not the property of, or licensed to the operator, are acknowledged on the website./i
        )
      ).toBeInTheDocument();
    });
  
    // Ensuring there's a warning about the consequences of unauthorized use of the website
    it('should warn about unauthorized use of the website', () => {
      // Check for a warning regarding unauthorized use and its potential legal consequences
      expect(
        screen.getByText(
          /Unauthorised use of this website may give rise to a claim for damages and\/or be a criminal offence./i
        )
      ).toBeInTheDocument();
    });
  
    // This is where you could add more tests for additional sections or specific content within the Terms component
  });