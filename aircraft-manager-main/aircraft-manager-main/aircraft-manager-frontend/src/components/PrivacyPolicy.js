import React from "react";
import { Box, Heading, Text } from "@chakra-ui/react";

const PrivacyPolicy = () => {
  return (
    <Box p="5">
      <Heading as="h1" mb="4">
        Privacy Policy
      </Heading>
      <Text fontSize="lg" mb="4">
        Welcome to our Privacy Policy
      </Text>
      <Text fontSize="md" mb="2">
        Your privacy is important to us. It is our policy to respect your
        privacy regarding any information we may collect from you across our
        website.
      </Text>
      <Text fontSize="md" mb="2">
        We only ask for personal information when we truly need it to provide a
        service to you. We collect it by fair and lawful means, with your
        knowledge and consent.
      </Text>
      <Text fontSize="md" mb="2">
        We don't share any personally identifying information publicly or with
        third-parties, except when required to by law.
      </Text>
      <Text fontSize="md" mb="2">
        Our website may link to external sites that are not operated by us.
        Please be aware that we have no control over the content and practices
        of these sites, and cannot accept responsibility or liability for their
        respective privacy policies.
      </Text>
      <Text fontSize="md" mb="2">
        You are free to refuse our request for your personal information, with
        the understanding that we may be unable to provide you with some of your
        desired services.
      </Text>
      <Text fontSize="md" mb="2">
        Your continued use of our website will be regarded as acceptance of our
        practices around privacy and personal information. If you have any
        questions about how we handle user data and personal information, feel
        free to contact us.
      </Text>
      <Text fontSize="md">This policy is effective as of 1 April 2024.</Text>
    </Box>
  );
};

export default PrivacyPolicy;
