import React, { useMemo, useState, useEffect } from 'react';
import { useTable, useSortBy, usePagination, useGlobalFilter } from 'react-table';
import { Table, Thead, Tbody, Tr, Th, Td, Box, Button, Input } from '@chakra-ui/react';

function MovementTable() {
    const [data, setData] = useState([]);
    const [filterInput, setFilterInput] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const fetchedData = [
                {
                    movementId: 1,
                    arrivalAirportId: 1,
                    originAirportId: 2,
                    arrivalDate: '2024-04-20 12:30',
                    departureDate: '2024-04-20 09:30',
                    aircraftId: 1,
                },
                {
                    movementId: 2,
                    arrivalAirportId: 2,
                    originAirportId: 1,
                    arrivalDate: '2024-04-21 16:00',
                    departureDate: '2024-04-21 13:00',
                    aircraftId: 2,
                },
            ];
            setData(fetchedData);
        };

        fetchData();
    }, []);

    const columns = useMemo(() => [
        { Header: 'Movement ID', accessor: 'movementId' },
        { Header: 'Arrival Airport ID', accessor: 'arrivalAirportId' },
        { Header: 'Origin Airport ID', accessor: 'originAirportId' },
        { Header: 'Arrival Date', accessor: 'arrivalDate' },
        { Header: 'Departure Date', accessor: 'departureDate' },
        { Header: 'Aircraft ID', accessor: 'aircraftId' },
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
        setGlobalFilter,  // 여기서 setGlobalFilter를 정의
        state: { pageIndex, pageSize },
    } = useTable(
        {
            columns,
            data,
            initialState: { pageIndex: 0 },
        },
        useGlobalFilter,
        useSortBy,
        usePagination,
    );

    const handleFilterChange = (e) => {
        const value = e.target.value || undefined;
        setGlobalFilter(value);  // setGlobalFilter를 사용
        setFilterInput(value);
    };

    return (
        <>
            <Box mb="4">
                <Input
                    value={filterInput}
                    onChange={handleFilterChange}
                    placeholder="Search all columns..."
                />
            </Box>
            <Table {...getTableProps()} variant="simple">
                <Thead>
                    {headerGroups.map((headerGroup) => (
                        <Tr {...headerGroup.getHeaderGroupProps()}>
                            {headerGroup.headers.map((column) => (
                                <Th {...column.getHeaderProps(column.getSortByToggleProps())}>
                                    {column.render('Header')}
                                    <span>
                                        {column.isSorted
                                            ? column.isSortedDesc
                                                ? ' 🔽'
                                                : ' 🔼'
                                            : ''}
                                    </span>
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
                                {row.cells.map((cell) => (
                                    <Td {...cell.getCellProps()}>{cell.render('Cell')}</Td>
                                ))}
                            </Tr>
                        );
                    })}
                </Tbody>
            </Table>
            <Box display="flex" justifyContent="space-between" mt="4">
                <Button onClick={previousPage} disabled={!canPreviousPage}>
                    Previous
                </Button>
                <Button onClick={nextPage} disabled={!canNextPage}>
                    Next
                </Button>
                <div>
                    Page {pageIndex + 1} of {pageOptions.length}
                </div>
                <select
                    value={pageSize}
                    onChange={(e) => setPageSize(Number(e.target.value))}
                >
                    {[10, 20, 30, 40, 50].map((size) => (
                        <option key={size} value={size}>
                            Show {size}
                        </option>
                    ))}
                </select>
            </Box>
        </>
    );
}

export default MovementTable;