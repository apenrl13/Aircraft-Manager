import React, { useState } from 'react';
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  Link as ChakraLink
} from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const formBackground = useColorModeValue("white", "gray.700");

  const baseUrl = 'http://localhost:5500/api'; 
  const table = 'userprofile';

  const handleLogin = async (e) => {
    try{
      e.preventDefault();
      const response = await axios.get(`${baseUrl}/${table}/?username=${username}&password=${password}`);
      if(response.data.success){
        let role = response.data.data[0].role
        if(role === 'admin'){
          alert(`You have successfully login as Administrator.`);
        }
        else{
          alert(`You have successfully login as ${role} Manager.`);
        }
        window.location.href = '/';
      }
      else{
        alert(response.data.message)
      }
    }
    catch(error){
      alert('Invalid username or passward.\nTry again or sign up for an account.');
    }
  };

  return (
    <Flex minHeight="100vh" align="center" justify="center" bg={formBackground}>
      <Box p={8} maxWidth="400px" borderWidth="1px" borderRadius="lg" boxShadow="lg">
        <Stack spacing={4} align="center" marginBottom={6}>
          <Heading>Sign In</Heading>
        </Stack>
        <Box>
          <form onSubmit={handleLogin}>
            <FormControl isRequired mb={3}>
              <FormLabel>Username</FormLabel>
              <Input 
                type="text" 
                placeholder="Enter username" 
                value={username} 
                onChange={(e) => setUsername(e.target.value)} 
              />
            </FormControl>
            <FormControl isRequired mb={3}>
              <FormLabel>Password</FormLabel>
              <Input 
                type="password" 
                placeholder="Enter password" 
                value={password} 
                onChange={(e) => setPassword(e.target.value)} 
              />
            </FormControl>
            <Stack spacing={6}>
              <Button 
                type="submit" 
                colorScheme="blue" 
                size="lg" 
                fontSize="md"
              >
                Sign In
              </Button>
            </Stack>
          </form>
          <Text mt={2} textAlign="center">
            Don't have an account?{" "}
            <ChakraLink as={RouterLink} to="/signup" color="blue.600">
              Sign up
            </ChakraLink>
          </Text>
        </Box>
      </Box>
    </Flex>
  );
};

export default Login;