import React, { useState } from "react";
import { Link as RouterLink, useNavigate } from "react-router-dom";
import {
  Flex,
  Box,
  IconButton,
  useDisclosure,
  Drawer,
  DrawerOverlay,
  DrawerContent,
  DrawerHeader,
  DrawerBody,
  VStack,
  Button,
  Image,
} from "@chakra-ui/react";
import { HamburgerIcon } from "@chakra-ui/icons";
import companyName from "../images/aircraftlogo.png";

function Header() {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [isLoggedIn, setIsLoggedIn] = useState(false); 
  const navigate = useNavigate(); 

  const handleLogout = () => {
    setIsLoggedIn(false); 
    navigate('/login'); 
  };

  return (
    <Flex
      as="header"
      align="center"
      justify="space-between"
      p="4"
      bg="blue.500"
      color="white"
      height="70px"
    >
      <IconButton
        icon={<HamburgerIcon />}
        onClick={onOpen}
        aria-label="Open Menu"
        variant="outline"
      />

      <Box flex="1" textAlign="center">
        <RouterLink to="/">
          <Image
            src={companyName}
            alt="Company Name"
            height="10%"
            maxH="180px"
            objectFit="contain"
            mx="auto"
            my="2"
          />
        </RouterLink>
      </Box>

      <Drawer isOpen={isOpen} placement="left" onClose={onClose}>
        <DrawerOverlay />
        <DrawerContent>
          <DrawerHeader borderBottomWidth="1px">Menu</DrawerHeader>
          <DrawerBody>
            <VStack spacing={4} align="stretch">
              <Button as={RouterLink} to="/" onClick={onClose}>Home</Button>
              <Button as={RouterLink} to="/dashboard" onClick={onClose}>Dashboard</Button>
              <Button as={RouterLink} to="/map" onClick={onClose}>Map</Button>
              <Button as={RouterLink} to="/editairports" onClick={onClose}>Edit Airports</Button>
              <Button as={RouterLink} to="/editaircrafts" onClick={onClose}>Edit Aircrafts</Button>
            </VStack>
          </DrawerBody>
        </DrawerContent>
      </Drawer>

      {/* 조건부 렌더링을 사용하여 로그인 상태에 따라 버튼을 표시합니다 */}
      {isLoggedIn ? (
        <Button
          onClick={handleLogout}
          variant="solid"
          colorScheme="blue"
          _hover={{ bg: "blue.600" }}
          _active={{ bg: "blue.700" }}
          size="md"
          mr="4"
        >
          Logout
        </Button>
      ) : (
        <>
          <Button
            as={RouterLink}
            to="/login"
            variant="solid"
            colorScheme="blue"
            _hover={{ bg: "blue.600" }}
            _active={{ bg: "blue.700" }}
            size="md"
            mr="4"
          >
            Login
          </Button>

          
        </>
      )}
    </Flex>
  );
}

export default Header;