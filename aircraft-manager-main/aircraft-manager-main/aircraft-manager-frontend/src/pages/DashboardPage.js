import React from 'react';
import { Routes, Route, NavLink } from 'react-router-dom';
import { Box, VStack, Button } from '@chakra-ui/react';
import AircraftTable from '../components/AircraftTable';
import AirportTable from '../components/AirportTable';
import MovementTable from '../components/MovementTable';

function DashboardPage() {
  return (
    <Box display="flex" bg="gray.100" height="100vh">
      {/* Sidebar Navigation */}
      <VStack
        spacing={4}
        align="stretch"
        p={5}
        bg="white"
        borderRight="1px solid gray"
        boxShadow="md"
        width="200px"
      >
        <NavLink to="/dashboard/aircrafts">
          <Button variant="solid" width="100%" colorScheme="blue">Aircrafts</Button>
        </NavLink>
        <NavLink to="/dashboard/airports">
          <Button variant="solid" width="100%" colorScheme="blue">Airports</Button>
        </NavLink>
        <NavLink to="/dashboard/movements">
          <Button variant="solid" width="100%" colorScheme="blue">Movements</Button>
        </NavLink>
      </VStack>
      {/* Main Content */}
      <Box flex="1" p={5}>
        <Routes>
          <Route index element={<AircraftTable />} />
          <Route path="aircrafts" element={<AircraftTable />} />
          <Route path="airports" element={<AirportTable />} />
          <Route path="movements" element={<MovementTable />} />
        </Routes>
      </Box>
    </Box>
  );
}

export default DashboardPage;