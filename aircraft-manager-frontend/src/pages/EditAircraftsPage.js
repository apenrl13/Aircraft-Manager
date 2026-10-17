import React, { useState, useEffect } from 'react';
import { Box, Button, Input, Stack } from '@chakra-ui/react';
import axios from 'axios';

function EditAircraftsPage() {
  const [formData, setFormData] = useState({
    tailNumber: '',
    aircraftType: '',
    status: '',
    location: '',
    userId: '1', // Default user ID
  });

  const [airports, setAirports] = useState([])

  const baseUrl = 'http://localhost:5500/api'; 
  const table = 'aircraft'; 


  const handelAddAircraft = async (e) => {
    if(!formData.aircraftType || !formData.aircraftType || !formData.status || !formData.location){
        e.preventDefault();
        alert("Missing Data Field");
    }
    else{
        try {
            const response = await axios.post(`${baseUrl}/${table}/`, formData);
            console.log('Response:', response.data);
            if (response.data.success) {
              console.log('Airport added successfully');
              window.location.href = '/dashboard/aircrafts';
            } else {
              console.error(response.data.message);
            }
          } catch (error) {
            console.error('Error adding airport:', error);
          }
    }
  };

  // Fetch airport locatoin for locations option
  const fetchLocations = async () => {
    try {
      const response = await axios.get(`${baseUrl}/airport/`);
      if (response.data.success) {
        setAirports(response.data.data)
      }
    } catch (error) {
    }
  };

  useEffect(() => {
    fetchLocations(); // Fetch airports on initial page load
  }, []); 

  return (
    <Box p={5}>
      <Stack spacing={4} align="center">
        <Input required placeholder="Tail Number" value={formData.tailNumber} onChange={(e) => setFormData({ ...formData, tailNumber: e.target.value })} />
        <Input required placeholder="Status" value={formData.status} onChange={(e) => setFormData({ ...formData, status: e.target.value })} />
        
        <label>
            Choose Aircraft Type:
            <select
                required value={formData.aircraftType}
                onChange={e => setFormData({...formData, aircraftType: e.target.value})}
                style={{ marginLeft: '10px' }}>
                <option value="" disabled={true}>Aircraft Type</option>
                <option value="A320">A320</option>
                <option value="A321">A321</option>
                <option value="A330">A330</option>
                <option value="A350">A350</option>
                <option value="B737">B737</option>
                <option value="B757">B757</option>
                <option value="B767">B767</option>
                <option value="B777">B777</option>
                <option value="B787">B787</option>
            </select>
        </label>
        <label>
            Choose Location:
            <select
                required value={formData.location}
                onChange={e => setFormData({...formData, location: e.target.value})}
                style={{ marginLeft: '10px' }}>
                <option value="" disabled={true}>Location</option>
                {airports.map(airport => (
                    <option key={airport.airportCode} value={airport.airportCode}>{airport.airportCode}</option>
                ))}
            </select>
        </label>
        <Button colorScheme="blue" onClick={handelAddAircraft}>Add Aircraft</Button>
      </Stack>
    </Box>
  );
}

export default EditAircraftsPage;
