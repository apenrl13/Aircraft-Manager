import React from "react";
import { Flex, Box, Heading, Text, Link, Divider } from "@chakra-ui/react";
import {
  FaEnvelope,
  FaPhone,
  FaFacebook,
  FaTwitter,
  FaInstagram,
} from "react-icons/fa";

const Footer = () => {
  return (
    <Box bg="gray.900" color="white" py="8">
      <Flex
        justify="space-between"
        align="center"
        direction={{ base: "column", md: "row" }}
        px="4"
      >
        <Box>
          <Heading as="h4" size="md" mb="2">
            Contact Us
          </Heading>
          <Text fontSize="sm" mb="4">
            Have questions or need assistance? Reach out to us!
          </Text>
          <Flex align="center" mb="2">
            <Box as={FaEnvelope} fontSize="lg" mr="2" />
            <Link
              href="mailto:contact@pythonairways.com"
              color="white"
              fontWeight="bold"
            >
              contact@pythonairways.com
            </Link>
          </Flex>
          <Flex align="center">
            <Box as={FaPhone} fontSize="lg" mr="2" />
            <Link href="tel:+11234567890" color="white" fontWeight="bold">
              +1 (123) 456-7890
            </Link>
          </Flex>
        </Box>
        <Divider
          display={{ base: "none", md: "block" }}
          orientation="vertical"
        />
        <Flex align="center" mt={{ base: "4", md: "0" }}>
          <Box textAlign={{ base: "center", md: "left" }}>
            <Text fontSize="sm" mb="2">
              &copy; 2024 Python Airways. All rights reserved.
            </Text>
            <Flex mb="2">
              <Link href="/privacy" color="white" mr="4" fontSize="sm">
                Privacy Policy
              </Link>
              <Link href="/terms" color="white" fontSize="sm">
                Terms of Service
              </Link>
            </Flex>
            <Flex>
              <Link href="https://www.facebook.com" isExternal>
                <Box as={FaFacebook} fontSize="3xl" mr="20" />
              </Link>
              <Link href="https://www.twitter.com" isExternal>
                <Box as={FaTwitter} fontSize="3xl" mr="20" />
              </Link>
              <Link href="https://www.instagram.com" isExternal>
                <Box as={FaInstagram} fontSize="3xl" mr="20" />
              </Link>
            </Flex>
          </Box>
        </Flex>
      </Flex>
    </Box>
  );
};

export default Footer;
