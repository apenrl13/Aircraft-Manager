import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Header from '../components/Header';
import { ChakraProvider } from '@chakra-ui/react';

// Mock the companyName import since it's a local image file. This avoids errors related to image loading in tests.
jest.mock('../images/aircraftlogo.png', () => 'aircraftlogo.png');

// Group tests related to the Header component
describe('Header Component', () => {
  // Helper function to wrap the component with necessary providers (ChakraProvider for styles and MemoryRouter for routing)
  const renderHeader = () =>
    render(
      <ChakraProvider>
        <MemoryRouter>
          <Header />
        </MemoryRouter>
      </ChakraProvider>
    );

  // Test to ensure the Header component renders without any errors
  it('should render without crashing', () => {
    renderHeader();
    // Checks if the hamburger menu button is rendered
    expect(screen.getByLabelText('Open Menu')).toBeInTheDocument();
    // Verifies the company logo is rendered with the correct src attribute
    expect(screen.getByAltText('Company Name')).toHaveAttribute('src', 'aircraftlogo.png');
    // Checks if the Login text, likely a button or link, is rendered
    expect(screen.getByText('Login')).toBeInTheDocument();
  });

  // Test to check if the drawer (menu) opens when the hamburger icon is clicked
  it('opens the drawer when the hamburger icon is clicked', () => {
    renderHeader();
    // Simulate a click event on the hamburger icon
    fireEvent.click(screen.getByLabelText('Open Menu'));
    // Verify if the Menu text appears, indicating the drawer is open
    expect(screen.getByText('Menu')).toBeInTheDocument();
  });

  // Test to ensure that the Header contains the correct navigation links
  it('contains the correct navigation links', async () => {
    renderHeader();
    // Simulate a click on the hamburger icon to open the drawer
    fireEvent.click(screen.getByLabelText('Open Menu'));
  
    // Asynchronously find each navigation link and verify its href attribute
    // This assumes that the navigation links are part of a dynamically loaded drawer menu
    const homeLink = await screen.findByText('Home').then((element) => element.closest('a'));
    const dashboardLink = await screen.findByText('Dashboard').then((element) => element.closest('a'));
    const mapLink = await screen.findByText('Map').then((element) => element.closest('a'));
  
    // Verify the href attribute of each link to ensure correct navigation
    expect(homeLink).toHaveAttribute('href', '/');
    expect(dashboardLink).toHaveAttribute('href', '/dashboard');
    expect(mapLink).toHaveAttribute('href', '/map');
  });

  // Test to verify the login button navigates to the login page
  it('has a login button that navigates to the login page', () => {
    renderHeader();
    // Find the login button and verify its navigation path
    const loginButton = screen.getByText('Login').closest('a');
    expect(loginButton).toHaveAttribute('href', '/login');
  });
});