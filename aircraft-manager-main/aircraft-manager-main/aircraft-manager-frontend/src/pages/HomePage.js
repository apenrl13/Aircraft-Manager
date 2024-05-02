import React from "react";
import {
  Box,
  Flex,
  Heading,
  Text,
  Button,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
} from "@chakra-ui/react";
import Hero from "../components/Hero";
import planes from "../images/planes.jpg";
import { Link as RouterLink } from "react-router-dom";

const HomePage = () => {
  return (
    <Box>
      <Hero
        title="Welcome to Python Airways"
        subtitle="Explore the world of aviation with us. Get real-time tracking, efficient fleet management, and more."
        image={planes}
        ctaText="Get Started"
        ctaLink="/signup"
      />

      {/* Services Section */}
      <Box py="12" bg="gray.100" textAlign="center">
        <Heading as="h2" size="xl" mb="8">
          Our Services
        </Heading>
        <Flex
          direction={{ base: "column", md: "row" }}
          justify="space-around"
          align="center"
          wrap="wrap"
        >
          {/* Service 1 */}
          <Box
            maxW="sm"
            p="6"
            shadow="md"
            borderWidth="1px"
            borderRadius="lg"
            bg="white"
          >
            <Heading as="h3" size="lg" mb="2">
              Real-time Tracking
            </Heading>
            <Text mb="4">
              Monitor your fleet in real-time with our advanced tracking system.
            </Text>
          </Box>
          {/* Service 2 */}
          <Box
            maxW="sm"
            p="6"
            shadow="md"
            borderWidth="1px"
            borderRadius="lg"
            bg="white"
            mt={{ base: "4", md: "0" }}
          >
            <Heading as="h3" size="lg" mb="2">
              Efficient Management
            </Heading>
            <Text mb="4">
              Manage your aircrafts and airports efficiently with our integrated
              platform.
            </Text>
          </Box>
          {/* Service 3 */}
          <Box
            maxW="sm"
            p="6"
            shadow="md"
            borderWidth="1px"
            borderRadius="lg"
            bg="white"
            mt={{ base: "4", md: "0" }}
          >
            <Heading as="h3" size="lg" mb="2">
              Secure Communication
            </Heading>
            <Text mb="4">
              Communicate securely with your team and partners using our
              encrypted messaging system.
            </Text>
          </Box>
        </Flex>
      </Box>

      {/* Table Comparison Section */}
      <Box py="12" bg="white" textAlign="center">
        <Heading as="h2" size="xl" mb="8">
          Why Choose Python Airways?
        </Heading>
        <Flex justify="center">
          <Box maxW="xl">
            <Table variant="simple" size="md" mx="auto">
              <Thead>
                <Tr>
                  <Th>Category</Th>
                  <Th>Python Airways</Th>
                  <Th>Competitor A</Th>
                  <Th>Competitor B</Th>
                </Tr>
              </Thead>
              <Tbody>
                <Tr>
                  <Td>Real-time Tracking</Td>
                  <Td>✔️</Td>
                  <Td>❌</Td>
                  <Td>✔️</Td>
                </Tr>
                <Tr>
                  <Td>Efficient Management</Td>
                  <Td>✔️</Td>
                  <Td>✔️</Td>
                  <Td>❌</Td>
                </Tr>
                <Tr>
                  <Td>Secure Communication</Td>
                  <Td>✔️</Td>
                  <Td>✔️</Td>
                  <Td>✔️</Td>
                </Tr>
              </Tbody>
            </Table>
          </Box>
        </Flex>
      </Box>

      {/* Call to Action Section */}
      <Flex
        align="center"
        justify="center"
        minHeight="60vh"
        bgGradient="linear(to-r, blue.700, blue.500)"
        color="white"
        px={{ base: "5", md: "10" }}
        flexDirection={{ base: "column", md: "row" }}
      >
        <Box flex="1">
          <Heading as="h2" size="xl" mb="4" textAlign="center">
            Ready to elevate your aviation experience?
          </Heading>
          <Text fontSize="lg" mb="8" textAlign="center">
            Sign up today and discover the future of aircraft management.
          </Text>
          <Flex justify="center">
            <Button
              as={RouterLink} // Use the RouterLink as the 'as' prop
              to="/signup"    // Set the routing path to the signup page
              colorScheme="orange"
              size="lg"
            >
              Get Started
            </Button>
          </Flex>
        </Box>
        <Box flex="1" display={{ base: "none", md: "block" }}>
          {/* Login Section */}
          <Box
            bg="blue.700"
            color="white"
            p="8"
            borderRadius="md"
            boxShadow="md"
          >
            <Heading as="h2" size="lg" mb="4" textAlign="center">
              Already have an account?
            </Heading>
            <Text fontSize="lg" mb="8" textAlign="center">
              Log in to access your account and manage your flights.
            </Text>
            <Flex justify="center">
              <Button
                colorScheme="orange"
                size="lg"
                as={RouterLink}
                to="/login"
              >
                Login
              </Button>
            </Flex>
          </Box>
        </Box>
      </Flex>
    </Box>
  );
};

export default HomePage;
