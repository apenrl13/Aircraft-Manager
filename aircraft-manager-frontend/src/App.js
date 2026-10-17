import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DashboardPage from "./pages/DashboardPage";
import HomePage from "./pages/HomePage";
import MapPage from "./pages/MapPage";
import AircraftListPage from "./pages/AircraftListPage";
import EditAircraftsPage from "./pages/EditAircraftsPage";
import EditAirportsPage from "./pages/EditAirportsPage";
import PrivacyPolicy from "./components/PrivacyPolicy";
import Terms from "./components/Terms";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { Box } from "@chakra-ui/react";

function App() {
  return (
    <Router>
      <Box className="App">
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/dashboard/*" element={<DashboardPage />} />
          <Route path="/map" element={<MapPage />} />
          <Route path="/editairports" element={<EditAirportsPage />} />
          <Route path="/privacy" element={<PrivacyPolicy />} />
          <Route path="/terms" element={<Terms />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/editaircrafts" element={<EditAircraftsPage/>}/>
          <Route path="/aircrafts/:location" element={<AircraftListPage />} />
        </Routes>
        <Footer />
      </Box>
    </Router>
  );
}

export default App;