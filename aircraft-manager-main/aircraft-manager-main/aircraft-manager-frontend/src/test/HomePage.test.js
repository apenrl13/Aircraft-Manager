// Importing necessary libraries and components for testing
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ChakraProvider } from '@chakra-ui/react'; // UI component library
import { BrowserRouter } from 'react-router-dom'; // For routing
import HomePage from '../pages/HomePage'; 

// Mocking external dependencies/components and image imports to isolate the test environment
jest.mock('../components/Hero', () => () => <div data-testid="hero">HeroMock</div>);
jest.mock('../images/planes.jpg', () => 'mocked-image-path');

// Grouping tests related to the HomePage component
describe('HomePage', () => {
  // Defining a specific test case for rendering the HomePage component
  test('renders HomePage component', () => {
    // Rendering the HomePage component wrapped in necessary providers for testing
    render(
      <BrowserRouter>
        <ChakraProvider>
          <HomePage />
        </ChakraProvider>
      </BrowserRouter>
    );

    // Verifying that the mocked Hero component is rendered successfully
    expect(screen.getByTestId('hero')).toBeInTheDocument();

    // Checking the presence of main sections' headings in the HomePage component
    expect(screen.getByText('Our Services')).toBeInTheDocument(); // Checks for "Our Services" heading
    expect(screen.getByText('Why Choose Python Airways?')).toBeInTheDocument(); // Checks for "Why Choose Python Airways?" heading
    expect(screen.getByText('Ready to elevate your aviation experience?')).toBeInTheDocument(); // Checks for "Ready to elevate your aviation experience?" heading

    // Verifying that a specific button with the text 'Get Started' is rendered
    expect(screen.getByText('Get Started')).toBeInTheDocument();
  });

  // Additional tests can be added here to check for other elements or interactions within the HomePage component
});