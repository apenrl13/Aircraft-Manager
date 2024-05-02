import React, { useMemo, useState, useEffect } from 'react';
import { useTable, useSortBy, usePagination, useGlobalFilter } from 'react-table';
import { Box, Table, Thead, Tbody, Tr, Th, Td, Button, Input } from '@chakra-ui/react';

function AirportTable() {
  const [data, setData] = useState([]);
  const [filterInput, setFilterInput] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const fetchedData = [
        { airportId: 1, airportCode: 'LAX', latitude: 33.941, longitude: -118.408, numAircraft: 10 },
        { airportId: 2, airportCode: 'JFK', latitude: 40.641, longitude: -73.778, numAircraft: 15 },
        { airportId: 3, airportCode: 'ORD', latitude: 41.974, longitude: -87.907, numAircraft: 20 },
        { airportId: 4, airportCode: 'SFO', latitude: 37.621, longitude: -122.379, numAircraft: 12 },
      ];
      setData(fetchedData);
    };

    fetchData();
  }, []);

  const columns = useMemo(() => [
    { Header: 'Airport ID', accessor: 'airportId' },
    { Header: 'Airport Code', accessor: 'airportCode' },
    { Header: 'Latitude', accessor: 'latitude' },
    { Header: 'Longitude', accessor: 'longitude' },
    { Header: 'Number of Aircraft', accessor: 'numAircraft' },
  ], []);

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    page,
    canPreviousPage,
    canNextPage,
    pageOptions,
    nextPage,
    previousPage,
    setPageSize,
    setGlobalFilter,
    state: { pageIndex, pageSize },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0 },
    },
    useGlobalFilter,
    useSortBy,
    usePagination
  );

  const handleFilterChange = e => {
    const value = e.target.value || undefined;
    setGlobalFilter(value);
    setFilterInput(value);
  };

  return (
    <Box>
      <Input
        value={filterInput}
        onChange={handleFilterChange}
        placeholder="Search all columns..."
      />
      <Table {...getTableProps()} variant="simple" tableLayout="fixed">
        <Thead>
          {headerGroups.map(headerGroup => (
            <Tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                <Th {...column.getHeaderProps(column.getSortByToggleProps())}>
                  {column.render('Header')}
                  <span>{column.isSorted ? (column.isSortedDesc ? ' 🔽' : ' 🔼') : ''}</span>
                </Th>
              ))}
            </Tr>
          ))}
        </Thead>
        <Tbody {...getTableBodyProps()}>
          {page.map((row) => {
            prepareRow(row);
            return (
              <Tr {...row.getRowProps()}>
                {row.cells.map(cell => (
                  <Td {...cell.getCellProps()}>{cell.render('Cell')}</Td>
                ))}
              </Tr>
            );
          })}
        </Tbody>
      </Table>
      <Box display="flex" justifyContent="space-between" alignItems="center" mt="4">
        <Button onClick={() => previousPage()} disabled={!canPreviousPage}>
          Previous
        </Button>
        <Box>
          Page {pageIndex + 1} of {pageOptions.length}
        </Box>
        <Button onClick={() => nextPage()} disabled={!canNextPage}>
          Next
        </Button>
        <select
          value={pageSize}
          onChange={e => setPageSize(Number(e.target.value))}
        >
          {[10, 20, 30, 40, 50].map(size => (
            <option key={size} value={size}>
              Show {size}
            </option>
          ))}
        </select>
      </Box>
    </Box>
  );
}

export default AirportTable;