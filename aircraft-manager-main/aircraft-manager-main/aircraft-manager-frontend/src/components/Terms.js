import React from "react";
import { Box, Heading, Text } from "@chakra-ui/react";

const Terms = () => {
  return (
    <Box p="5">
      <Heading as="h1" mb="4">
        Terms and Conditions
      </Heading>
      <Text fontSize="md" mb="2">
        Welcome to our website. If you continue to browse and use this website,
        you are agreeing to comply with and be bound by the following terms and
        conditions of use.
      </Text>
      <Text fontSize="md" mb="2">
        The content of the pages of this website is for your general information
        and use only. It is subject to change without notice.
      </Text>
      <Text fontSize="md" mb="2">
        Neither we nor any third parties provide any warranty or guarantee as to
        the accuracy, timeliness, performance, completeness, or suitability of
        the information and materials found or offered on this website for any
        particular purpose.
      </Text>
      <Text fontSize="md" mb="2">
        Your use of any information or materials on this website is entirely at
        your own risk, for which we shall not be liable. It shall be your own
        responsibility to ensure that any products, services, or information
        available through this website meet your specific requirements.
      </Text>
      <Text fontSize="md" mb="2">
        This website contains material which is owned by or licensed to us. This
        material includes, but is not limited to, the design, layout, look,
        appearance, and graphics. Reproduction is prohibited other than in
        accordance with the copyright notice, which forms part of these terms
        and conditions.
      </Text>
      <Text fontSize="md" mb="2">
        All trademarks reproduced in this website, which are not the property
        of, or licensed to the operator, are acknowledged on the website.
      </Text>
      <Text fontSize="md">
        Unauthorised use of this website may give rise to a claim for damages
        and/or be a criminal offence.
      </Text>
    </Box>
  );
};

export default Terms;
