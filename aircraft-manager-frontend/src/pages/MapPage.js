import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { Box, Button } from '@chakra-ui/react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const starIconUrl = require('../images/starIcon.png');
const starIcon = new L.Icon({
  iconUrl: starIconUrl,
  iconSize: [25, 25],
  iconAnchor: [12, 25],
  popupAnchor: [1, -34],
});

function MapPage() {
  const [airports, setAirports] = useState([]);
  const [selectedAirport, setSelectedAirport] = useState(null);

  const baseUrl = 'http://localhost:5500/api'; 
  const apiSetName = 'airport';

  const fetchAirports = async () => {
    try {
      const response = await axios.get(`${baseUrl}/${apiSetName}/`);
      console.log('API response:', response.data);
      if (response.data.success) {
        setAirports(response.data.data);
      } else {
        console.error(response.data.message);
      }
    } catch (error) {
      console.error('Error fetching airports:', error);
    }
  };

  useEffect(() => {
    fetchAirports(); // Fetch airports on initial page load
  }, []); 

  const handleEditAirports = () => {
    window.location.href = '/editairports'; 
  };

  return (
    <Box p={5}>
      <Button colorScheme="blue" color="white" mb={4} onClick={handleEditAirports}>
        Edit Airports
      </Button>
      <MapContainer center={[39.8283, -98.5795]} zoom={4} style={{ height: '600px', width: '100%' }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {airports.map((airport) => (
          <Marker
            key={airport.airportId}
            position={[parseFloat(airport.latitude), parseFloat(airport.longitude)]}
            icon={starIcon}
            eventHandlers={{
              click: () => {
                setSelectedAirport(airport);
              },
            }}
          >
            {selectedAirport === airport && (
              <Popup onClose={() => setSelectedAirport(null)}>
                <Box>{airport.airportCode}</Box>
                <Link to={`/aircrafts/${airport.airportCode}`}>
                  <Button colorScheme="blue" size="xs" mt={2}>
                    View Aircrafts
                  </Button>
                </Link>
              </Popup>
            )}
          </Marker>
        ))}
      </MapContainer>
    </Box>
  );
}

export default MapPage;