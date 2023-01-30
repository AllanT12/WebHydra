import * as React from 'react';
import Link from '@material-ui/core/Link';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import { useTheme } from '@material-ui/core/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';

function createData(time, amount) {
  return { time, amount };
}

const data = [
  createData('00:00', 0),
  createData('03:00', 300),
  createData('06:00', 600),
  createData('09:00', 800),
  createData('12:00', 1500),
  createData('15:00', 2000),
  createData('18:00', 2400),
  createData('21:00', 2400),
  createData('24:00', undefined),
];

const Packets = (props) =>{
  const { devices } = props;
   const theme = useTheme();
  if (devices === null|| devices?.length === 0) {return <p>Can not find any packets, sorry</p>;}else {
    return (
        <React.Fragment>

      <ResponsiveContainer>
        <LineChart
          data={data}
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        >
          <XAxis
            dataKey="time"
            stroke={theme.palette.text.secondary}
            style={theme.typography.body2}
          />
          <YAxis
            stroke={theme.palette.text.secondary}
            style={theme.typography.body2}
          >
            <Label
              angle={270}
              position="left"
              style={{
                textAnchor: 'middle',
                fill: theme.palette.text.primary,
                ...theme.typography.body1,
              }}
            >
              Sales ($)
            </Label>
          </YAxis>
          <Line
            isAnimationActive={false}
            type="monotone"
            dataKey="amount"
            stroke={theme.palette.primary.main}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>

            <ResponsiveContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Packet info</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {devices?.map((packet) => (
                  <TableRow key={packet?.id}>
                    <TableCell>{packet?.packetinfo}</TableCell>
                  </TableRow>
              ))}
            </TableBody>
          </Table>
                </ResponsiveContainer>
        </React.Fragment>
    );
  }
}
export default Packets;
