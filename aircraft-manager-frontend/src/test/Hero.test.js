import React from 'react';
// Importing utilities from React Testing Library for rendering and querying the component
import { render, screen } from '@testing-library/react';
// Importing BrowserRouter for routing capabilities required by the Hero component
import { BrowserRouter as Router } from 'react-router-dom';
// Importing the Hero component to be tested
import Hero from '../components/Hero'; 

// Mocking static file imports, which Jest cannot handle natively. This redirects any import of 'planes.jpg' to a mock image path.
jest.mock('../images/planes.jpg', () => 'path/to/mockImage.jpg');

// Describes a testing suite for the Hero component
describe('Hero Component', () => {
  // Defines a reusable function to render the Hero component with optional props for different test cases
  const renderHeroComponent = (props = {}) => {
    render(
      // Wraps the Hero component in a Router since the component likely uses routing features like Link or NavLink
      <Router>
        <Hero {...props} />
      </Router>
    );
  };

  // Test case for rendering the Hero component with its default props
  it('renders correctly with default props', () => {
    // Renders the Hero component without any custom props, implying default props are used
    renderHeroComponent();
    // Assertions to check if the default text content is rendered as expected
    expect(screen.getByText('Welcome to Python Airways')).toBeInTheDocument();
    expect(screen.getByText('Explore the world of aviation with us. Get real-time tracking, efficient fleet management, and more.')).toBeInTheDocument();
    expect(screen.getByText('Get Started')).toBeInTheDocument();
    // Assertion to check if the image source is the mocked path, ensuring the component handles static images correctly
    expect(screen.getByRole('img')).toHaveAttribute('src', 'path/to/mockImage.jpg');
  });

  // Test case for rendering the Hero component with custom props to ensure it's properly responsive to props
  it('renders correctly with custom props', () => {
    // Defines custom props to pass to the Hero component
    const customProps = {
      title: 'Custom Title',
      subtitle: 'Custom subtitle content.',
      ctaText: 'Custom CTA',
      ctaLink: '/custom-link',
      image: 'path/to/customImage.jpg',
    };
    
    // Renders the Hero component with the specified custom props
    renderHeroComponent(customProps);
    // Assertions to check if the component correctly renders content based on the custom props
    expect(screen.getByText(customProps.title)).toBeInTheDocument();
    expect(screen.getByText(customProps.subtitle)).toBeInTheDocument();
    expect(screen.getByText(customProps.ctaText)).toBeInTheDocument();
  });
});