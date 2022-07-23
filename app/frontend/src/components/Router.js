import { BrowserRouter, Route, Routes } from "react-router-dom";
import SignIn from "./SignIn";
import Dashboard from "./dashboard/Dashboard";
import SignUp from "./SignUp";

function AllRoutes() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<SignIn />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/register" element={<SignUp />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}
export default AllRoutes;
