import { makeStyles } from '@material-ui/core/styles';
import { Button, useTheme } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  defaultButton: {
    backgroundColor: theme.palette.primary.main,
    borderColor: theme.palette.primary.main,
    color: theme.palette.contrast.white
  }
}));

export const SendButton = ({name}) => {
  const theme = useTheme()
  const classes = useStyles(theme);
  return (
    <>
      <Button className={classes.defaultButton}>{name}</Button>
    </>
  );
}