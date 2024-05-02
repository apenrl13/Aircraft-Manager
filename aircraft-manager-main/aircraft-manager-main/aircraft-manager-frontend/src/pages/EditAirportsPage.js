import React, { useState } from 'react';
import { Box, Button, Input, Stack } from '@chakra-ui/react';
import axios from 'axios';

function EditAirportsPage() {
  const [formData, setFormData] = useState({
    airportCode: '',
    latitude: '',
    longitude: '',
    numAircraft: '',
    userId: '1', // Default user ID
  });

  const baseUrl = 'http://localhost:5500/api'; 
  const apiSetName = 'airport'; 

  const handleAddAirport = async () => {
    try {
      const response = await axios.post(`${baseUrl}/${apiSetName}/`, formData);
      console.log('Response:', response.data);
      if (response.data.success) {
        console.log('Airport added successfully');
        window.location.href = '/map';
      } else {
        console.error(response.data.message);
      }
    } catch (error) {
      console.error('Error adding airport:', error);
    }
  };

  return (
    <Box p={5}>
      <Stack spacing={4} align="center">
        <Input placeholder="Airport Code" value={formData.airportCode} onChange={(e) => setFormData({ ...formData, airportCode: e.target.value })} />
        <Input placeholder="Latitude" value={formData.latitude} onChange={(e) => setFormData({ ...formData, latitude: e.target.value })} />
        <Input placeholder="Longitude" value={formData.longitude} onChange={(e) => setFormData({ ...formData, longitude: e.target.value })} />
        <Input placeholder="Number of Aircraft" value={formData.numAircraft} onChange={(e) => setFormData({ ...formData, numAircraft: e.target.value })} />
        <Button colorScheme="blue" onClick={handleAddAirport}>Add Airport</Button>
      </Stack>
    </Box>
  );
}

export default EditAirportsPage;
